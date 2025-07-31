''''''


#12.3.1 创建Pygame窗口及相应用户输入
import sys

import pygame

# # 方式2：导入特定子模块，可以直接使用，但不推荐这样更加麻烦，如果以后需要用到其他函数的话，模块pygame中的event
# from pygame import display
#
# display.set_mode()

#一个模块中，可以包含子模块，单独的函数，类，类中的函数
#所以也就可以：
# 语法	示例	说明
# 模块.函数()	pygame.quit()	调用模块中的函数
# 模块.常量	pygame.QUIT	访问模块中的常量
# 模块.子模块	pygame.display	访问子模块
# 模块.类	pygame.Rect	访问模块中的类
# 模块.类.方法()	pygame.Surface.fill()	调用类的方法

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """
        初始化游戏并创建游戏资源。

        #1 初始化Pygame引擎
        #2 创建游戏窗口并设置标题
        """
#1
        pygame.init()
        # 初始化Pygame所有子模块，确保后续功能可用
        # 在AlienInvasion类中初始化Pygame是资源管理的最佳实践，
        # 能确保游戏对象在可用状态下创建，避免隐蔽的错误。
#2
        self.screen = pygame.display.set_mode((1200, 800))
        # 说明display是子模块，并不是类（很好区分）
        # [以下关于导入方式和作用域的说明很准确]
        # 导入方式不同：
        #   使用import pygame时，需要通过模块名前缀访问内容
        #   使用from pygame import display可直接访问display，但不推荐
        # 作用域规则：
        #   import pygame只将模块名引入命名空间
        #   子模块（如display）需要通过pygame.访问

        #总结此处用到第9章 类 中的第9.4.4 导入整个模块 中的知识点，导入了整个模块，使用语法module_name.ClassName访问需要的类
        pygame.display.set_caption('Alien Invasion')#在模块的子模块中调用set_caption这个函数

    def run_game(self):
        """开始游戏的主循环"""
#3
        while True:
            # 监视键盘和鼠标事件
#4
            for event in pygame.event.get():  # 从事件队列取出所有待处理事件 #event是子模块，模块.子模块.方法()
#5          在这里，event等价于这个函数get，然后
                if event.type == pygame.QUIT:  # 过滤出关闭窗口事件
                    sys.exit()  # 立即终止程序
            # 让最近绘制的屏幕可见。   #调用pygame这个模块中的常量QUIT

            # pygame.event.get()
            # 作用：从Pygame事件队列中获取所有待处理事件
            # 返回值：返回一个Event对象列表（按发生时间排序）
            # 重要特性：
            # 调用后会清空事件队列（类似
            # "读取后删除"）
            # 如果没有新事件，返回空列表[
#6
            pygame.display.flip()#在模块的子模块中调用flip这个函数
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()#创建ai这个实例
    ai.run_game()       #调用这个实例中的方法

# 如果是正式项目、可复用模块、库代码，必须加 if __name__ == '__main__':
# 如果是临时脚本、纯工具函数、明确不会被导入的代码，可以省略（但仍建议加上）
# 🚀 最佳实践：无论什么情况，都加上 if __name__ == '__main__':，避免未来踩坑

"""
Pygame 的命名风格总结
类型	示例	命名风格	是否符合 PEP8？
模块	pygame.display, pygame.event	小写	✅ 符合（模块应小写）
函数	pygame.quit(), pygame.init()	小写	✅ 符合（函数应 snake_case）
类	pygame.Surface, pygame.Rect	PascalCase	✅ 符合（类应 PascalCase）
常量	pygame.QUIT, pygame.K_SPACE	大写	✅ 符合（常量应 UPPER_CASE）"""


'''
#在1处，调用函数pygame.init()来初始化背景设置，让Python能够正确地工作
#在2处，调用pygame.display.set_mode()来创建一个显示窗口，
#实参(1200,800)是一个元组，指定了游戏窗口的尺寸————宽1200像素、高800像素（可自行调整这些属性值）。
#将这个显示窗口赋给属性self.screen，让这个类中的所有方法都能够使用它

#  赋给属性self.screen 的对象是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。
#在这个游戏中，每个元素（如外星人或飞船）都是一个surface。
# display.set.mode()返回的surface表示整个游戏窗口。激活游戏的动画循环后，
# 每经过一次循环都将自动重绘这个surface，将用户输入触发的所有变化都反映出来。


#  这个游戏由方法run_game()控制，该方法包含一个不断运行的while循环（见3），而这个循环包含一个事件
#循环以及管理屏幕更新的代码。事件是用户玩游戏时执行的操作，如按键或移动鼠标。为程序响应事件，可编写一
#个“事件循环”，以 侦听 事件并根据发生的事件类型执行合适的任务。
#在4处，for循环就是一个事件循环

#  为访问Pygame检测到的事件，我们使用了函数Pygame.event.get()。这个函数返回一个列表，其中包含他
#在上一次被调用后发生的所有事件。所有键盘和鼠标事件都将导致这个for循环运行。在这个循环中，我们将编写一
#系列if语句来检测并相应特定的事件。例如，当玩家单击游戏窗口的关闭按钮时，将检测pygame.QUIT事件，进
#而调用sys.exit()来退出游戏（见5）。

#  在6处调用了pygame.display.flip()，命令Pygame让最近绘制的屏幕可见。在这里，它在每次执行while
#循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。我们移动游戏元素时，pygame.display.fli
#p()将不断更新屏幕，以显示元素的新位置，并且在原来的位置隐藏元素，从而营造平滑移动的效果。

#  在这个文件末尾，创建一个游戏实例并调用run_game()。这些代码放在一个if代码块中，仅当直接运行该文件
#时，它们才会执行。如果此时运行alien_invasion.py，将看到一个空的Pygame窗口。
'''

from ship import Ship


#12.3.2 设置背景色
import sys

import pygame

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

#1
        # 设置背景色
        self.bg_color = (230, 230, 230)#一种浅灰色
        #(255,0,0)红色 (0,255,0)绿色 (0,0,255)蓝色

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

#2
            # 每次循环时都重新绘制
            self.screen.fill(self.bg_color)

            # 让最近绘制的屏幕可见。
            pygame.display.flip()
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()


#在1处，我们生成了一种浅灰色，将它赋给了self.bg_color
#在2处，调用方法fill()用这种背景色填充屏幕。方法fill()用于处理surface，只接受一个实参，一种颜色（颜色可以自己调），所以不能五颜六色
''''''


'''

#12.3.3 创建设置类

import sys

import pygame

#1
from settings import Settings

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
#2
        self.settings = Settings()

#3
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))

        #self.screen = pygame.display.set_mode((1200, 800)) 将这行代码替换成上面的代码
        pygame.display.set_caption('Alien Invasion')


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

#4
            # 每次循环时都重新绘制
            self.screen.fill(self.settings.bg_color)

            # 每次循环时都重新绘制
            #self.screen.fill(self.bg_color) 将这行代码替换成上面的代码

            # 让最近绘制的屏幕可见。
            pygame.display.flip()
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()


#  在1处，导入Setting类，
#在2处，调用了pygame.init()，在创建一个Settings实例并将其赋给self.settings
#在3处，使用了self.setting的属性 screen_width和screen_height。
#在4处，填充屏幕时，也使用了self.settings来访问背景色。
'''

'''
#12.4 添加飞船图像
#12.4.1 创建Ship类
#具体例子在ship.py中

#12.4.2 在屏幕上绘制飞船

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))

        #self.screen = pygame.display.set_mode((1200, 800)) 将这行代码替换成上面的代码
        pygame.display.set_caption('Alien Invasion')

#1
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘制屏幕
            self.screen.fill(self.settings.bg_color)
#2
            self.ship.blitme()

            # 每次循环时都重绘制屏幕
            #self.screen.fill(self.bg_color) 将这行代码替换成上面的代码

            # 让最近绘制的屏幕可见。
            pygame.display.flip()
if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()


#在1处，创建屏幕后创建一个Ship实例，调用Ship()时，必须提供一个参数：一个AlienInvasion实例。在这里，self指向的是当前AlienInvasion实例


#12.5 重构：方法_check_events()和__update_screen()
#重构既有代码。重构旨在简化既有代码的结构，使其容易扩展。run_game()拆分成两个辅助方法（helper methods）：_check_events()和__update_screen()
'''

'''

#12.5.1 方法_check_events()  && #12.5.2 方法_update_screen()


import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))

        #self.screen = pygame.display.set_mode((1200, 800)) 将这行代码替换成上面的代码
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
#1        
            self._check_events()
            self._update_screen()

#             # 每次循环时都重绘制屏幕 包装成函数，此处不在写
#             self.screen.fill(self.settings.bg_color)
#             self.ship.blitme()
#
# #             # 每次循环时都重绘制屏幕
# #             #self.screen.fill(self.bg_color) 将这行代码替换成上面的代码
#
#             # 让最近绘制的屏幕可见。
#             pygame.display.flip()

#2
    def _check_events(self):
        """相应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        # 每次循环时都重绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

#在1处，调用当前类的方法，用句点表示法，并指定变量名self和要调用的方法的名称
#在2处，新增方法_check_events，并将检查玩家是否单击了关闭窗口按钮的代码移到该方法中。
'''

'''

#12.6 驾驶飞船
#让玩家能够左右驾驶飞船，编写代码，在用户按左或右箭头作出相应

#12.6.1 响应按键
#  每当用户按按键时，都将在Pygame中注册一个事件。时间都是通过方法pygame.event.get()获取的，因此需要在方法_check_events()中指定要检查哪些的类型的事件。每次按键都被注册为一个KEYDOWN事件。

#  Pygame检测到KEYDOWN事件时，需要检查按下的是否触发行动的键，例如，如果玩家按下的右箭头键，就增大飞船的rect.centerx的值，将飞船向右移动：

import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))

        #self.screen = pygame.display.set_mode((1200, 800)) 将这行代码替换成上面的代码
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """相应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x+=10
                    # 向右移动飞船
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x-=10
                    # 向左移动飞船
                    #但是无论向左还是向右，都是不连贯，要按一下动一下，无法达到按持续按下，然后持续移动效果


    def _update_screen(self):
        # 每次循环时都重绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
    
'''
#12.6.2 允许持续移动

