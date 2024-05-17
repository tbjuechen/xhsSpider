from TaskGenerator import TaskGenerator
from PhotoDownloader import PhotoDownloader
from female_classifier import FemaleClassifier
import config


if __name__ == '__main__':
    # tg = TaskGenerator()
    # # tg.head_page_init()
    
    # pd = PhotoDownloader()
    
    for i in range(10):
        tg = TaskGenerator()
         # tg.head_page_init()
    
        pd = PhotoDownloader()
        tg.head_page_init()
        tasks = list(tg.generate_task_url())
        for task in tasks:
            pd.new_task(task)
    classifier = FemaleClassifier()
    classifier.classify_images()