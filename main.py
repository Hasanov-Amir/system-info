import utils

hint = '''
после входа дает выбор:
1 распечатать список установленных программ     ✓
2 печатает только айпи адресс ОС                ✓
3 проверить RDP протокол (открыт/закрыт)        ✓
4 сколько процентов батарейки осталось и время  ✓
5 статус Windows Security                       ✓
6 в системе найти все пустые папки              ✓
7 список языков                                 ✓
8 выход                                         ✓
'''

if __name__ == '__main__':
    while True:
        num = int(input(f"{hint}\nChoose a number: "))

        if num == 8:
            break

        try:
            result = eval(f"utils.{utils.__all__[num-1]}()")

            if isinstance(result, str):
                print(result)
            else:
                for i in result:
                    print(i)

            choice = int(input(f"\nReturn? (1/0): "))

            if not choice:
                break

        except:
            print("Enter a valid number.")
