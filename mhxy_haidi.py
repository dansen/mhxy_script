import sys

from mhxy import *


class Haidi(MhxyScript):

    def do(self, chaseWin = (-3, 5.8 + 0)):
        # 流程任务 领取任务后起点
        def do():
            if datetime.datetime.now().minute >= 41:
                self._flag=False
            def reach():
                return Util.locateCenterOnScreen(r'resources/haidi/select.png')
            Util.doubleClick(chaseWin[0], chaseWin[1])
            reachPos = reach()
            times = 0
            while reachPos is None:
                if not self._stopCheck():
                    sys.exit(0)
                reachPos = reach()
                cooldown(1)
                times += 1
                # 新的一个战斗或完成一轮
                if times >= 6:
                    log("恢复流程")
                    # 10秒左右还没进入战斗 重新追踪
                    Util.leftClick(chaseWin[0], chaseWin[1])
                    times = 0
            cooldown(0.5)
            pyautogui.leftClick(reachPos.x, reachPos.y)
        escapeBattleDo(do)

# 副本 进入第一个副本为起点
if __name__ == '__main__':
    pyautogui.PAUSE = 0.5
    log("start task....")
    while datetime.datetime.now().hour != 21:
        cooldown(2)
    Haidi().do((-3, 6))

