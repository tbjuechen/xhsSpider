import os

STARTPAGE = 'https://www.xiaohongshu.com/explore'
MAXTASK = 100

DOWNPATH = os.path.join(os.path.expanduser('~'),'Downloads','集美')
INTIMEOUT = 0
MODELPATH = './classifier_model/resnet50/epoch_39.pth'
CLASSIFIERPATH = os.path.join(os.path.expanduser('~'),'Downloads','集美','分类')