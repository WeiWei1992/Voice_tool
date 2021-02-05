import delete_logs
import os
import time
from datetime import datetime
import re
#from Audio_Accuracy.file import *
from file import *
import tkinter
from tkinter import *
import tkinter.messagebox
#from Audio_Accuracy.test import main
from test import main


from tkinter import Image
from tkinter.filedialog import askopenfilename,askopenfilenames,askdirectory,asksaveasfilename
import threading
from tkinter import scrolledtext

#from Audio_Accuracy.test import *
from test import *

import os
import time
from datetime import datetime
import re
import pyaudio
import wave
#from Audio_Accuracy.conver_encod import convertUTF8ToANSI
from conver_encod import convertUTF8ToANSI
#from Audio_Accuracy.operate_excel import creat_excel,write_excel
from operate_excel import creat_excel,write_excel
#from Audio_Accuracy.conver_encod import rb_to_utf
from conver_encod import rb_to_utf
#from Audio_Accuracy.send_email import my_send
#from Audio_Accuracy.send_email import my_send
from send_email import my_send
#adb拉取日志到指定路径下
# os.system('adb devices')
# os.system('adb pull /tmp/uai_log.txt D:\download')
# print("拉去文件结束")
#from Audio_Accuracy.file import get_txt_line
from file import get_txt_line,get_parameter

import logging
import logging.config
CON_LOG='config\\log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


def is_chinese(instr): #判断输入的设备id是否是空和是否有汉字
    zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
    match = zhmodel.search(instr)
    if match:
        logging.info("设备id中有中文，返回空字符串即可")
        return ""
    else:
        logging.info("没有中文，返回字符串")
        return instr
        #print('没有包含中文')

def cut_email(email):
    email_list=re.split('[, ：; ]',email.strip())
    return email_list
    # print(email_list_tmp)
    # for i in range(len(email_list_tmp)):
    #     email_list.append(email_list_tmp[i])
    # #print(email_list)
    # return email_list


def get_now_time_millisecond():
    #获取当前时间的毫秒级时间戳
    t = time.time()
    my_time=int(round(t * 1000)) # 毫秒级时间戳
    return my_time

def my_main():
    root = Tk()
    root.title("智能音响语音识别自动化工具")
    # root.geometry("500x300+750+200")  #窗口位置,这里四个参数分别为：宽、高、左、上
    sw = root.winfo_screenwidth()
    # print(sw)
    # 得到屏幕宽度
    sh = root.winfo_screenheight()
    # print(sh)
    # 得到屏幕高度
    ww = 100
    wh = 100
    # 窗口宽高为100
    # x = (sw - ww) / 2
    # y = ((sh - wh) / 5) * 4
    # print("X: ",x)
    # print("Y: ",y)

    x = 700
    y = 600
    #y = ((sh - wh) / 4) * 3
    # root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
    root.geometry("%dx%d+%d+%d" % (x, y, ww, wh))
    # root.minsize(560,545)
    # Label(root,text="zuopin").grid(row=0)  #使用这种方法没有办法剧中
    title = Label(root, text="              智能音箱语音自动化测试工具V2.2", compound=CENTER, font=("微软雅黑", 20))
    title.grid(row=0, columnspan=3, sticky=E + W)

    def I_do(deviceid,email,wake_path,jiaohu_path,excel_path,wait_time,device_version=None):

        #预处理deviceid，如果有汉字或者是空，则赋值为空
        deviceid=is_chinese(deviceid)
        email=cut_email(email)

        wake_path=wake_path+'/'
        jiaohu_path=jiaohu_path+'/'

        excel_file = creat_excel(excel_path)
        logging.info("创建excel文件，保存测试结果：" + str(excel_file))
        xiaoyou_path_wav_new, jiaohu_path_wav, jiaohu_path_txt = get_file_all(wake_path, jiaohu_path)
        # print(jiaohu_path_wav)
        logging.info("文件预处理完毕,打印下处理后返回的结果")
        logging.info("xiaoyou_path_wav_new:")
        logging.info(xiaoyou_path_wav_new)
        logging.info("jiaohu_path_wav:")
        logging.info(jiaohu_path_wav)
        logging.info("jiaohu_path_txt:")
        logging.info(jiaohu_path_txt)

        for i in range(len(jiaohu_path_wav)):
            # print(jiaohu_path_wav[i])
            #向GUI页面写入数据
            j=int(i)+1
            tmp1="执行第 "+str(j)+" 条用例\n"
            text.insert(END,tmp1)
            text.see(END)
            tmp=jiaohu_path_wav[i]
            res="测试用例: "+tmp+'\n'
            text.insert(END,res)
            text.see(END)

            now_millisecond_time = get_now_time_millisecond()
            time.sleep(3)

            # 播放唤醒语音
            logging.info("播放唤醒词： " + str(xiaoyou_path_wav_new[i]))
            play_wav(xiaoyou_path_wav_new[i])
            # 等待时间，需要根据经验设置等待时间
            time.sleep(3)
            # 播放交互语音
            logging.info("播放交互词： " + str(jiaohu_path_wav[i]))
            play_wav(jiaohu_path_wav[i])
            # 等待一会
            logging.info("等待(s)........."+str(wait_time))
            logging.info("这个过程期间如果小优没有识别正确，你可以人工干预......")
            time.sleep(wait_time)
            # 拉取日志
            logging.info("开始拉取日志....")
            logging.info("  deviceid:   "+deviceid)
            file_path, filter_log_path ,audio_path= load_log(deviceid)

            # print("=======log地址======")
            logging.info("====log地址====")
            # print('file_path',file_path)
            logging.info("file_path: " + str(file_path))
            # print('filter_log_path',filter_log_path)
            logging.info("filter_log_path: " + str(filter_log_path))
            logging.info("audio_path: "+str(audio_path))

            time.sleep(3)
            get_log_time_after(file_path, filter_log_path, now_millisecond_time)

            time.sleep(2)

            is_wake, wake_line, is_indenty, identy_str, real_str, nlp_test = log_check(filter_log_path,
                                                                                       jiaohu_path_txt[i])
            logging.info("结果写入excel中: " + str(excel_file))
            write_excel(excel_file, xiaoyou_path_wav_new[i], jiaohu_path_wav[i], jiaohu_path_txt[i],
                        file_path, filter_log_path,audio_path,is_wake, wake_line, is_indenty, identy_str, real_str, nlp_test)
            time.sleep(3)
        # print("测试结束，发送邮件")
        logging.info("测试结束，发送邮件")
        # msg_to = ['1508691067@qq.com']
        # my_send(excel_file,msg_to)
        #device_version=None
        my_send(excel_file, email,device_version)
        text.insert(END,"测试结束")
        text.see(END)

    def I_do_no_adb(wake_path,jiaohu_path,wait_time):
        wake_path = wake_path + '/'
        jiaohu_path = jiaohu_path + '/'
        xiaoyou_path_wav_new, jiaohu_path_wav, jiaohu_path_txt = get_file_all_no_adb(wake_path, jiaohu_path)

        logging.info("处理后的唤醒词与交互词语料")
        logging.info(xiaoyou_path_wav_new)
        logging.info(jiaohu_path_wav)

        for i in range(len(jiaohu_path_wav)):
            # print(jiaohu_path_wav[i])
            #向GUI页面写入数据
            j=int(i)+1
            tmp1="执行第 "+str(j)+" 条用例\n"
            text.insert(END,tmp1)
            text.see(END)
            tmp=jiaohu_path_wav[i]
            res="测试用例: "+tmp+'\n'
            text.insert(END,res)
            text.see(END)

            # 播放唤醒语音
            logging.info("播放唤醒词： " + str(xiaoyou_path_wav_new[i]))
            play_wav(xiaoyou_path_wav_new[i])
            # 等待时间，需要根据经验设置等待时间
            time.sleep(3)
            # 播放交互语音
            logging.info("播放交互词： " + str(jiaohu_path_wav[i]))
            play_wav(jiaohu_path_wav[i])
            # 等待一会
            logging.info("等待(s)........."+str(wait_time))
            logging.info("这个过程期间如果小优没有识别正确，你可以人工干预......")
            time.sleep(wait_time)

            # time.sleep(3)

        text.insert(END,"测试结束")
        text.see(END)






    def click():
        logging.info("点击开始测试按钮，开始测试")
        deviceid = Deviceid_entry.get()
        #print("deviceid:", deviceid)
        logging.info("获取到的设备id："+deviceid)
        email = email_entry.get()
        #print("email: ", email)
        logging.info("获取到的email: "+email)

        device_version=Device_version_entry.get()
        logging.info("获取到的设备版本号："+device_version)

        wake_path=wake_path_entry.get()
        print("wake_path: ",wake_path)

        jiaohu_path=jiaohu_path_entry.get()
        print("jiaohu_path: ",jiaohu_path)

        # jiaohu_path_txt_path=jiaohu_path_txt_entry.get()
        # print("jiaohu_path_txt_path:",jiaohu_path_txt_path)

        excel_path=path_excel_entry.get()
        print("excel_path: ",excel_path)

        wait_time=wait_time_entry.get()
        print("wait_time: ",wait_time)
        wait_time=int(wait_time)

        #添加一个线程
        th=threading.Thread(target=I_do,args=(deviceid,email,wake_path,jiaohu_path,excel_path,wait_time,device_version))
        th.setDaemon(True)  #设置守护线程，主线程结束后，该线程也要结束
        th.start()

    def click_2():
        #读取配置文件参数
        logging.info("点击开始测试按钮，开始测试")
        deviceid=get_parameter('deviceid')
        logging.info("获取到的设备id：" + deviceid)

        email = get_parameter('Email')
        # print("email: ", email)
        logging.info("获取到的email: " + email)

        device_version = get_parameter('deviceversion')
        logging.info("获取到的设备版本号：" + device_version)

        wake_path = get_parameter('wake_path')
        logging.info("获取到的唤醒路径： "+wake_path)


        jiaohu_path = get_parameter('jiaohu_path')
        logging.info("获取到的交互词路径： "+str(jiaohu_path))

        excel_path = get_parameter('excel_path')
        logging.info("获取到的excel路径： "+excel_path)


        wait_time = get_parameter('wait_time')
        logging.info("获取到的等待时长是： "+wait_time)

        wait_time = int(wait_time)
        # 添加一个线程
        th = threading.Thread(target=I_do,args=(deviceid, email, wake_path, jiaohu_path, excel_path, wait_time, device_version))
        th.setDaemon(True)  # 设置守护线程，主线程结束后，该线程也要结束
        th.start()

    def click_3():

        wake_path = wake_path_entry.get()
        if wake_path:
            logging.info("UI页面获取到的唤醒词路径是： "+wake_path)
        else:
            logging.info("UI页面没有获取到wake_path,在配置文件中获取")
            wake_path = get_parameter('wake_path')
            logging.info("配置文件获取到的唤醒路径： " + wake_path)

        jiaohu_path = jiaohu_path_entry.get()
        if jiaohu_path:
            logging.info("UI页面获取到的交互词路径是： "+jiaohu_path)
        else:
            logging.info("UI页面没有获取到jiaohu_path,在配置文件中获取")
            jiaohu_path = get_parameter('jiaohu_path')
            logging.info("配置文件获取到的交互词路径是： "+jiaohu_path)

        wait_time = wait_time_entry.get()
        if wait_time:
            logging.info("UI页面获取到的等待时长是: "+str(wait_time))
        else:
            logging.info("UI页面没有获取到等待时间，在配置文件中获取")
            wait_time = get_parameter('wait_time')
            logging.info("配置文件中获取到的等待时间是： "+str(wait_time))
        wait_time=int(wait_time)
        th = threading.Thread(target=I_do_no_adb,args=(wake_path,jiaohu_path,wait_time))
        th.setDaemon(True)  # 设置守护线程，主线程结束后，该线程也要结束
        th.start()




        # wait_time = wait_time_entry.get()
        # print("wait_time: ", wait_time)
        #
        # wait_time = int(wait_time)
        # logging.info("获取到的等待时长是： " + str(wait_time))

        # pass



    deviceid_tmp = StringVar(value='xxxx(设备id)')

    Deviceid_label = Label(root, text="设备id ", foreground="white", background="blue")
    Deviceid_label.grid(sticky=E, padx=10, pady=10)
    Deviceid_entry = Entry(root, textvariable=deviceid_tmp, width=70)
    # e2 = Entry(root)
    Deviceid_entry.grid(row=1, column=1, sticky=W)

    device_version = StringVar()
    Device_version_label = Label(root, text="设备版本 ", foreground="white", background="blue")
    Device_version_label.grid(sticky=E, padx=10, pady=10)
    Device_version_entry = Entry(root, textvariable=device_version, width=70)
    # e2 = Entry(root)
    Device_version_entry.grid(row=2, column=1, sticky=W)


    email_tmp = StringVar(value='319910390@qq.com;')
    email_label = Label(root, text="Email ", foreground="white", background="blue")
    email_label.grid(sticky=E, padx=10, pady=10)
    email_entry = Entry(root, textvariable=email_tmp, width=70)
    email_entry.grid(row=3, column=1, sticky=W)




    path = StringVar()
    wake_path_label=Label(root,text="唤醒词路径",foreground="white", background="blue")
    wake_path_label.grid(sticky=E, padx=10, pady=10)
    wake_path_entry=Entry(root,textvariable=path,width=70)
    wake_path_entry.grid(row=4,column=1,sticky=W)
    def selectPath():
        path_=askdirectory()
        path.set(path_)
        print(path_)
        #wake_path_tmp=path_
    Button(root, text='路径选择', command=selectPath).grid(row=4, column=2)

    path_jiaohu = StringVar()
    jiaohu_path_label=Label(root,text="交互词路径",foreground="white", background="blue")
    jiaohu_path_label.grid(sticky=E, padx=10, pady=10)
    jiaohu_path_entry=Entry(root,textvariable=path_jiaohu,width=70)
    jiaohu_path_entry.grid(row=5,column=1,sticky=W)
    def selectPath_jiaohu():
        path_jiaohu_tmp=askdirectory()
        path_jiaohu.set(path_jiaohu_tmp)
        #print(path_jiaohu)
        #wake_path_tmp=path_
    Button(root, text='路径选择', command=selectPath_jiaohu).grid(row=5, column=2)


    path_excel = StringVar()
    path_excel_label = Label(root, text="输出excel路径", foreground="white", background="blue")
    path_excel_label.grid(sticky=E, padx=10, pady=10)
    path_excel_entry = Entry(root, textvariable=path_excel, width=70)
    path_excel_entry.grid(row=6, column=1, sticky=W)

    def selectPath_excel():
        path_excel_tmp = askdirectory()
        path_excel.set(path_excel_tmp)

    Button(root, text='路径选择', command=selectPath_excel).grid(row=6, column=2)


    wait_time=StringVar(value='60')
    wait_time_label=Label(root,text='等待时间(s)',foreground='white',background='blue')
    wait_time_label.grid(sticky=E,padx=10,pady=10)
    wait_time_entry=Entry(root,textvariable=wait_time,width=70)
    wait_time_entry.grid(row=7,column=1,sticky=W)




    # text=Text(root,width=60,height=10)
    # text.grid(row=6,column=1, sticky=W)
    # text.insert(INSERT,' weiwei\n')
    text=scrolledtext.ScrolledText(root,width=80,height=10)
    text.grid(row=8,column=1,columnspan=2,sticky=W)
    #text.insert(INSERT,'wew\n')


    click_btn = Button(root, text="开始测试", command=click)
    click_btn.grid(row=9,column=0)

    click_btn_2=Button(root,text="开始测试(配置文件模式)",command=click_2)
    click_btn_2.grid(row=9,column=1)

    click_btn_3=Button(root,text="开始测试(无adb)",command=click_3)
    click_btn_3.grid(row=9,column=2)


    root.mainloop()

if __name__=="__main__":
    my_main()
    # 判断一段文本中是否包含简体中文
    #import re

    #askopenfilename()
    # https://blog.csdn.net/zjiang1994/article/details/53513377/
    # def selectPath():
    #     path_=askdirectory()
    #     path.set(path_)
    # root=Tk()
    # path=StringVar()
    #
    # Label(root,text="目标路径: ").grid(row=0,column=0)
    # Entry(root,textvariable=path).grid(row=0,column=1)
    # Button(root,text='路径选择',command=selectPath).grid(row=0,column=2)
    # #
    # root.mainloop()
