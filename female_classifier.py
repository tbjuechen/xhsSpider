from PIL import Image
import torch
from torchvision import transforms, models
import os
import shutil
import torch.nn as nn
import config

class FemaleClassifier:
    def __init__(self, model_path=config.MODELPATH, device=None):
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        
        self.device = device if device else torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        
        # 加载训练好的模型
        self.model = models.resnet50(pretrained=False)
        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 2)  # 假设有两个类别：女性和非女性
        
        self.model = self.model.to(self.device)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()  # 设置模型为评估模式
        
        self.class_names = ['female', 'not_female']
        
        self.result_dir = config.CLASSIFIERPATH
        os.makedirs(self.result_dir, exist_ok=True)
        for class_name in self.class_names:
            os.makedirs(os.path.join(self.result_dir, class_name), exist_ok=True)
    
    def predict(self, image_path=config.DOWNPATH):
        image = Image.open(image_path).convert('RGB')
        image = self.preprocess(image)
        image = image.unsqueeze(0)  # 增加一个维度，形成 batch 大小为 1 的张量
        image = image.to(self.device)

        # 进行预测
        with torch.no_grad():
            outputs = self.model(image)
            _, preds = torch.max(outputs, 1)
            return preds.item()
    
    def classify_images(self, input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                image_path = os.path.join(input_folder, filename)
                prediction = self.predict(image_path)
                class_name = self.class_names[prediction]
                result_path = os.path.join(self.result_dir, class_name, filename)
                shutil.copy(image_path, result_path)
        print("Classification complete. Results saved in the '{}' directory.".format(self.result_dir))
