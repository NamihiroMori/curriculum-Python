while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
        print('↓')
        if number == 1:
            int('hoge')
        if number == 2:
            list = ['a', 'b', 'c']
            print(list[3])
        if number == 3:
            print('例外を発生させませんでした')
        if number == 4:
            print('終了します')
            break

    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
    except ValueError as e:
        print('Value Error')
        print(e.args)
    except IndexError as e:
        print('Index Error')
        print(e.args)
    finally:
        if number != 4:
            print('↓')
            print('もう一度選択しましょう')

print('↓')
print('無限ループを終了します')