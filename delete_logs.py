
import time
import os
res=os.getcwd()
result_tmp_1_path = os.path.join(res, 'Logs/runlog.log')
print("删除runlog.log: ",result_tmp_1_path)
# result_tmp_path_1
# print("res: ",res)
# print("result_tmp_path_1:",result_tmp_path_1)
# print("result_tmp_1_path",result_tmp_1_path)
if os.path.isfile(result_tmp_1_path):
    print("删除runlog.log")
    os.remove(result_tmp_1_path)

audio_path=os.path.join(res,'Logs/audio')
original_path=os.path.join(res,'/Logs/original_log')
result_path=os.path.join(res,'/Logs/result_log')


import logging
import logging.config
CON_LOG='config\\log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
import shutil


#logging.info("首先清除下日志文件")
print("首先清除下日志文件")
audio_path=os.path.join(res,'Logs/audio')
print(audio_path)
del_list_audio=os.listdir(audio_path)
#print("del_list_audio: ",del_list_audio)

original_log_path=os.path.join(res,'Logs/original_log')
del_original=os.listdir(original_log_path)

# result_history_path=os.path.join(res,'Logs/result_history')
# del_result_history=os.listdir(result_history_path)

result_log_path=os.path.join(res,'Logs/result_log')
def_result_log=os.listdir(result_log_path)

# del_list=[]
# del_list.append(del_list_audio)
# del_list.append(del_original)
# del_list.append(del_result_history)
# del_list.append(def_result_log)

for f in del_list_audio:
    logging.info("删除: "+str(audio_path))
    #print("删除： ",str(audio_path))
    #print("f: ",f)
    file_path=os.path.join(audio_path,f)
    if os.path.isfile(file_path):
        os.remove(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)

for f in del_original:
    #print("f: ",f)
    logging.info("删除： "+str(original_log_path))
    #print("删除： ",str(original_log_path))
    file_path=os.path.join(original_log_path,f)
    if os.path.isfile(file_path):
        os.remove(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)


for f in def_result_log:
    #print("f: ",f)
    logging.info("删除： "+str(result_log_path))
    #print("删除： ",str(result_log_path))
    file_path=os.path.join(result_log_path,f)
    if os.path.isfile(file_path):
        os.remove(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)


# def delete_files():
#     logging.info("首先清除下日志文件")
#     audio_path=os.path.join(res,'Logs/audio')
#     print(audio_path)
#     del_list_audio=os.listdir(audio_path)
#     #print("del_list_audio: ",del_list_audio)
#
#     original_log_path=os.path.join(res,'Logs/original_log')
#     del_original=os.listdir(original_log_path)
#
#     # result_history_path=os.path.join(res,'Logs/result_history')
#     # del_result_history=os.listdir(result_history_path)
#
#     result_log_path=os.path.join(res,'Logs/result_log')
#     def_result_log=os.listdir(result_log_path)
#
#     # del_list=[]
#     # del_list.append(del_list_audio)
#     # del_list.append(del_original)
#     # del_list.append(del_result_history)
#     # del_list.append(def_result_log)
#
#     for f in del_list_audio:
#         logging.info("删除: "+str(audio_path))
#         #print("f: ",f)
#         file_path=os.path.join(audio_path,f)
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#
#     for f in del_original:
#         #print("f: ",f)
#         logging.info("删除： "+str(original_log_path))
#         file_path=os.path.join(original_log_path,f)
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#
#
#     for f in def_result_log:
#         #print("f: ",f)
#         logging.info("删除： "+str(result_log_path))
#         file_path=os.path.join(result_log_path,f)
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#

