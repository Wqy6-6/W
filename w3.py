import random


def play_number_bomb():
    """数字炸弹游戏主函数"""
    print("🎮 === 数字炸弹游戏 ===")

    # 设置游戏难度
    print("请选择难度：")
    print("1. 简单（1-50）")
    print("2. 普通（1-100）")
    print("3. 困难（1-200）")

    while True:
        try:
            level = int(input("请输入难度编号（1 -3）："))
            if level == 1:
                max_num = 50
            elif level == 2:
                max_num = 100
            elif level == 3:
                max_num = 200
            else:
                print("请输入1-3之间的数字！")
                continue
            break
        except ValueError:
            print("请输入有效的数字！")

    # 生成随机数
    bomb = random.randint(1, max_num)
    attempts = 0
    min_range, max_range = 1, max_num

    print(f"\n💣 炸弹已埋好！范围：1-{max_num}")
    print("开始拆弹吧！")

    while True:
        try:
            attempts += 1
            guess = int(input(f"\n第{attempts}次尝试，请输入数字（{min_range}-{max_range}）："))

            # 检查输入是否在有效范围内
            if guess < min_range or guess > max_range:
                print(f"请输入{min_range}-{max_range}之间的数字！")
                continue

            # 判断猜测结果
            if guess == bomb:
                print(f"\n💥 BOOM! 你用了{attempts}次猜中了炸弹数字 {bomb}！")
                if attempts <= 5:
                    print("🎉 太厉害了！你是拆弹专家！")
                elif attempts <= 10:
                    print("👍 不错的表现！")
                else:
                    print("下次加油！")
                break
            elif guess < bomb:
                min_range = guess + 1
                print(f"💣 炸弹数字比 {guess} 大")
            else:
                max_range = guess - 1
                print(f"💣 炸弹数字比 {guess} 小")

        except ValueError:
            print("请输入有效的数字！")


# 游戏主循环
if __name__ == "__main__":
    play_again = True

    while play_again:
        play_number_bomb()

        # 询问是否再玩一次
        choice = input("\n再玩一次？（输入 y 继续，其他键退出）：").lower()
        play_again = (choice == 'y' or choice == 'yes')

    print("感谢游玩数字炸弹游戏！")


