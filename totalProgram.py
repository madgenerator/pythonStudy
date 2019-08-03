import random

# 1~N까지 합과 평균
def calSumAverage():
    firstnumber=input("input First Number: ")
    lastnumber=input("input Second Number: ")

    sum=0
    mylist = []

    for i in range(int(firstnumber),int(lastnumber)+1):
        mylist.append(i)
    #print(mylist)

    for num in mylist:
        sum = sum+num
    print(sum)

    average = sum/len(mylist)
    print (average)


def calculator():
    calculator = True
    while calculator:
        x=int(input("enter the First number: "))
        y=int(input("enter the Second number: "))
        z=input("enter operation (+ - * / ): ")
        if (z=='+'):
            print(x+y)
        elif (z=='-'):
            print(x-y)
        elif (z=='/'):
            if(y==0):
                print("Can Not devided by '0'")
            else:
                print(x/y)
        elif (z=='*'):
            print(x*y)
        
        end = input("END Calculate? Y/N:")
        if(end=='y' or end =='Y'):
            calculator = False

def storyMaker():
    c1 = input("주인공 1 이름을 입력하세요 :")
    c2 = input("주인공 2 이름을 입력하세요 :")
    place = input("장소 이름을 입력하세요 :")

    type=random.randint(1, 3)
    if type==1:
        print("""{0}은 창밖을 조심히 바라보았다.
    짙은 남색과 보라색이 뒤섞인,애매모호한 색의 하늘과 하늘에 떠 있는 조그마한 하얀색 별들에게
    {0}는 알 수 없는 깊은 이질감을 느꼈다.살짝 열린 창문 사이로 달콤하고도 시큼한 꽃의 향기가 조근조근 맡아져왔다.
    다른 세계에 와 있다는 것이 새삼 느껴졌다.{0}은 망토 주머니에 들어 있던 별 조각을 조금 흔들었다.
    한기가 조금이나마 가시는 듯 했다.숨을 내쉴 때마다 투명하면서도 불투명한 입김이, 조금씩 나왔다.
    모험을 시작하기 좋은 날이었다. {0}는, 그의 옷자락을 약하게 움켜쥐었다.
    주머니 속 별이 순간 반짝였다.""".format(c1,c2,place))

    elif type==2:
        print("""{0}은 {1}이 가지고 있던 열쇠를 가볍게 낚아챘다. 역시나. 그가 예상했던 대로였다. {1}은 공장의 주인이였다.
    코끝으로 간간히 들이마셔지는 매연과 연기에 목이 메어 왔다. {0}은 가벼운 휘파람을 불며 철문을 열었다.
    그곳에는 이 모든 일을 해결할 열쇠, {2}가 놓여 있었다. 황금처럼 반짝이는 모습으로.""".format(c1,c2,place))

    elif type==3:
        print("""{0}은 혼란을 느꼈다. 잠시 만년필을, 아니 자신의 증조-증조 할머니께서 가지고 계셨던 오래된 만년필을 잡고
    자신의 이름을 종이에 써 본 것이 끝인데, {0}은 어느새 오묘하고도 이상하리만큼 뒤틀린 공간 속에서 정처 없이 떠돌고
    있었다. {0}은 차근차근 기억을 되돌려 보기 시작하였다. {0}이 펜을 잡기도 전에 그녀의 언니 {1}은 그 만년필을
    보고 씨익 소름끼치게 웃어 보였다. 왜지? 순간 {0}의 기억이 뒤틀렸다. 배경도, 떨리는 그녀의 손도.
    모두 일그러져 보였다. 그리고 그녀는 자신이 어디 와 있는지에 대한 답을 알았다.
    그녀는, {1}, 아니 악몽의 여신 플루토가 만들어낸 새로운 세상에 와 있었다.""".format(c1,c2,place))
        
    type = random.randint(1,3)
    if type==1:
        print("""그러나 사실 {0}은 {1}의 부모님의 원수였기 때문에, {1}은 복수를 하려고 {2}에서
    {0}을 만났던 것이었다! 그것도 모르는 {0}은 {1}에게 소중한 호떡 보물을 주었고,
    잠자던 사이 마법이 풀린 {0}은 {2}에서 추방되고 말았다!! {1}은 이제 {2}를 지배하게
    되었고, {2}의 모든곳이 호떡으로 변했다는 슬픈 이야기 흑흑ㅠㅠㅠ""".format(c1,c2,place))
    elif type==2:
        print("""그러나 {0}은 {1}이 재채기를 하자 갑자기 변신하여 불을 뿜기 시작했고, {1}의 고향인
    {2}로 날아가버렸다! {1}은 빨리 {0}을 원래대로 돌려놓아야만 했는데, 마법 지팡이가
    {2}에 있다는걸 알고는 아! 이것이 나의 운명인가!! 라고 말하며 엉엉 울고 말았다.
    그 사이 {0}은 {2}에 도착하고 말았고, 불을 뿜어 {2}가 불타려고 하는 그 때!!
    {1}의 눈물이 얼음으로 변해서 {2}를 지켜주었다!! {0}은 추워서 다시 원래대로 돌아왔고
    {1}은 다시는 재채기를 하지 않았다는 재미있는 이야기~""".format(c1,c2,place))
    elif type==3:
        print("""그러나 {0}은 사실 기계 인간이었고 그것도 모르는 {1}은 전기 충격기로 {0}을 쏴버린
    그 순간!! 지지지작!!!! 크와앙~ {0}은 본모습을 드러내고 만 것이다! 놀란 {1}은 비행선을
    타고 인간들만 사는 나라 {2}로 향하기 시작했고 기계 왕국은 {0}의 신호를 받아 {2}로
    총출동하게 되었다!! 아무것도 모르는 {2}의 사람들은 무방비로 기계 왕국의 공격을 받아
    쑥대밭이 되고 말았고, 늦게 도착해버린 {1}은 불타버린 {2} 나라에서 망연자실 눈물을 흘리며
    복수를 다짐하고 1편이 끝~~ ~""".format(c1,c2,place))    


print("만능 프로그램에 오신걸 환영합니다~ copyright by 준봉")
while(True):
    print("어떤 기능을 원하시나요??")
    userInput = input("1.계산기 , 2.평균구하기, 3.이야기만들기 :")

    if(userInput=="1"):
        calculator()
    elif(userInput=="2"):
        calSumAverage()
    elif(userInput=="3"):
        storyMaker()
    else:
        print("잘못된 입력입니다 Error!")

    answer = input("계속 하시겠습니까?? Y/N :")
    if(answer=="N" or answer == "n"):
        break








