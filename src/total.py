# module import가 안되는 문제 해결
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import audio
import driver
import time

def main(*argv, **kwargv):
    m = audio.Musicplayer()
    d = driver.Driver()
    d.input_thread.start()


    # 주행 명령을 추가
    m.play("start")
    m.play("car moving", terminate=False)
    m.wait_finish()
    d.add_command(50, 1.75, 0, 'forward') 
    d.execute_commands()
 

    m.play("now parking")
    m.play("beep effect", repeat=100, terminate=False)
    d.add_command(50, 0.6, -1, 'backward')
    d.add_command(50, 0.15, 0, 'backward')
    d.add_command(50, 0.6, 1, 'backward')
    d.add_command(50, 0.1, 0, 'backward')
    d.execute_commands()
    m.play("complete parking")
    m.wait_finish()

    time.sleep(1)

    m.play("leave parking")
    m.play("car moving", terminate=False)
    m.wait_finish()
    d.add_command(50, 0.45, 1, 'forward')
    d.add_command(50, 0.2, 0, 'forward')
    d.add_command(50, 0.5, -1, 'forward')
    d.add_command(50, 0.1, 0, 'forward')
    d.execute_commands()
    m.play("complete leaving")
    m.wait_finish()

    time.sleep(1)

    m.play("car moving", terminate=False)
    m.wait_finish()
    d.add_command(50, 1.8, 0, 'forward')
    d.execute_commands()
    m.play("car stop")
    m.play("finish", terminate=False)
    m.wait_finish()

    d.input_thread.join()
    
    return

if __name__ == '__main__':
    main(*sys.argv[1:]) 