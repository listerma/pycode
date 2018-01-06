# -*- coding: utf-8 -*-
# @Date    : 2018-01-06 22:22:48
# @Author  : brkstone

import random


class roleplay(object):
    """
    定义英雄&小兵的共同特性
    生命值：hp
    攻击力：dmge
    移动速度：mov
    攻击：attk()
    """

    def __init__(self, hp, dmge, mov):
        self.hp = hp
        self.dmge = dmge
        self.mov = mov

    def __str__(self):
        return ('生命值：{}|攻击力：{}|移动速度：{}').format(self.hp, self.dmge, self.mov)

    # 普通攻击
    def attk(self, role):
        # 士兵攻击
        if isinstance(role, hero):
            role.hp -= self.dmge
            print('{}生命力：{}'.format(self.name, self.hp))
            print('{}生命力：{}'.format(role.name, role.hp))
        # 英雄攻击
        elif isinstance(role, soldier):
            role.hp -= self.dmge
            print('{}生命力：{}'.format(self.name, self.hp))
            print('{}生命力：{}'.format(role.name, role.hp))

    # 移动
    def moveto(self):
        pass

    # 判断是存活，存活返回1，否则返回0
    def islive(self):
        if self.hp <= 0:
            return 0
        else:
            return 1


class hero(roleplay):
    """
    英雄
    生命值：500
    攻击力：50
    移动速度：25
    魔法值：200
    """

    def __init__(self, mp=200, name='yingxiong'):
        super(hero, self).__init__(hp=500, dmge=50, mov=25)
        self.mp = mp
        self.name = name

    def __str__(self):
        return ('生命值：{}|攻击力：{}|移动速度：{}|魔法值：{}').format(self.hp, self.dmge, self.mov, self.mp)

    def cast_attk(self, role):
        # 设定 魔法攻击/60mp
        role.hp -= self.dmge * 1.5
        print('英雄发动魔法攻击！')
        self.mp -= 60
        # print('{}生命力：{}|魔法值：{}'.format(self.name, self.hp, self.mp))
        # print('{}生命力：{}'.format(role.name, role.hp))


class soldier(roleplay):
    """
    士兵
    生命值：150
    攻击力：5
    移动速度：10
    """

    def __init__(self, name='shibing'):
        super(soldier, self).__init__(hp=150, dmge=20, mov=10)
        self.name = name


# 游戏运行 yx -- 英雄  xb -- 小兵
def each_round(yx, xb):
    pass
chse = input('请选择你的角色[1.英雄  2.士兵 (Enter退出)]:')
while chse in set(['1', '2', '']):
    if chse == '1':
        player = hero()
        robot = soldier()
        print('初始化状态')
        print('英雄：', player)
        print('士兵：', robot, '\n', '==' * 20)
        ba_round = 1
        while player.hp != 0 and robot.hp != 0:
            print('==' * 10, '第{}回合'.format(ba_round), '==' * 10)
            if player.mp >= 60 and player.hp > 0:
                do_id = input('你可以选择1.攻击2.移动3.魔法攻击[默认1]')
                if do_id == '' or do_id == '1':
                    player.attk(robot)
                elif do_id == '2':
                    player.moveto()
                else:
                    player.cast_attk(robot)
                if robot.islive():
                    if random.randint(1, 2) == 1:
                        robot.attk(player)
                    else:
                        robot.moveto()
                    if player.islive():
                        ba_round += 1
                    else:
                        print('英雄阵亡')
                else:
                    print('士兵阵亡')
            elif player.mp < 60 and player.hp > 0:
                do_id = input('你可以选择1.攻击2.移动[默认1]')
                if do_id == '' or do_id == '1':
                    player.attk(robot)
                elif do_id == '2':
                    player.moveto()
                if robot.islive():
                    if random.randint(1, 2) == 1:
                        robot.attk(player)
                    else:
                        robot.moveto()
                    if player.islive():
                        ba_round += 1
                    else:
                        print('英雄阵亡')
                else:
                    print('士兵阵亡')
            print('{}|生命力：{}|魔法值：{}'.format(player.name, player.hp, player.mp))
            print('{}|生命力：{}'.format(robot.name, robot.hp))
        chse = input('继续游戏?请选择你的角色[1.英雄  2.士兵 (Enter退出)]:')

    elif chse == '2':
        pass
        break
    elif chse == '':
        print('游戏结束！')
        break
else:
    print('输入错误')
