# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
#import time
from pywinauto import findwindows
from pywinauto import application

os.system('chcp 65001')
#
# if os.system('tasklist | findstr "OrmChart.exe"') is None:
#     os.system("taskkill -im OrmChart.exe -f")
#     print("ormchart exit")
# if os.system('tasklist | findstr "OrmChart.exe"') is None:
#     os.system("taskkill -im ClientProxy.exe -f")
#     print("ormchart proxy")

# time.sleep(1)
# dir_path = "C:/Program Files (x86)/OrmChart_Qa"
#
# if os.path.exists(dir_path):
#     shutil.rmtree(dir_path)


# subprocess.call(["C:\\Users\\kimjiheon\\Desktop\\OrmChartSetup_Qa_3.0.0.658.exe"])
procs = findwindows.find_elements()

for proc in procs:
    print(f"{proc} / 프로세스 : {proc.process_id}")

app = application.Application(backend='win32')

#app.start("C:\\Users\\kimjiheon\\Desktop\\OrmChartSetup_Qa_3.0.0.658.exe")
app.connect(process=1672)

# dlg = app['오름차트(Qa)'] # 변수에 노트패드 윈도우 어플리케이션 객체를 할당
# dlg.print_control_identifiers() # 노트패드의 컨트롤 요소를 트리로 모두 출력