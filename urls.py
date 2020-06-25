from flask import Blueprint, send_file
import os



urls= Blueprint('urls', __name__)

@urls.route('/sys_img/<pic_path>',methods=['GET','POST'])
def returnPic(pic_path):
    fileDir = os.path.join(os.path.dirname(os.path.realpath('__file__')),'static')
    targetPath=os.path.join(fileDir,pic_path)

    return send_file(targetPath, mimetype='image/png') #, video/mp4 



