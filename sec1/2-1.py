all_place = ["札幌","東京","横浜","大阪","名古屋","福岡"]
wait_place = ["札幌","大阪"]
get_place = ["横浜"]

for place in all_place:
    if place in get_place:
        print(place + "のチケットが当選しました！")
    elif place in wait_place:
        print(place + "のチケットは結果待ち")
    else:
        print(place + "のチケットは落選しました")

# get_placeとwait_placeを連結し、間に"と"を挿入した文字列を作成し、出力
joined_place = 'と'.join(get_place + wait_place)
print("{}のチケットが当選しました！".format(joined_place))