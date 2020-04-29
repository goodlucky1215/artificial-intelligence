#iloc
#integer positon를 통해 값을 찾을 수 있다. label로는 찾을 수 없다
#loc
#label 을 통해 값을 찾을 수 있다. integer position로는 찾을 수 없다.
#ix
#integer position과 label모두 사용 할 수 있다. 만약 label이 숫자라면 label-based index만 된다.


#다음과 같이 label이 숫자로 이루어진 Series가 있다면,
#>>> s = pd.Series(np.nan, index=[49,48,47,46,45, 1, 2, 3, 4, 5])
#>>> s
#49   NaN
#48   NaN
#47   NaN
#46   NaN
#45   NaN
#1    NaN
#2    NaN
#3    NaN
#4    NaN
#5    NaN

#s.iloc[:3]은 integer position을 이용하므로 1-3번째 row를 반환한다. 즉 그 순서가 중요한거야!![:5]면 49,48,47,46,45까지 반환하겠지!
#s.loc[:3]은 label을 이용하므로 1-8번째 row를 반환할 것 이다. 즉 idex 에 값이 있으면 반환한다는 거야. 만약에 s.loc[:46] 이어도 1-8다 반환.
#s.loc[:6]라면 index=[49,48,47,46,45, 1, 2, 3, 4, 5]에는 6이라는 숫자가 없으니깐 아예 반환XXX
#s.ix[:3]은 label이 숫자인경우 label-based indexing을 따르므로 .loc 처럼 1-8번째 row를 반환할 것이다. 둘다 가능
#우선적으로 loc에  맞추지만, s.ix[:6]라면 49,48,47,46,45, 1 까지 반환 한다는거야.

하지만, 만일 label이 아래와같이 숫자와 문자로 이루어져 있다면,


>>> s2 = pd.Series(np.nan, index=['a','b','c','d','e', 1, 2, 3, 4, 5])
>>> s2.index.is_mixed() # index is mix of types
True
>>> s2.ix[:6] # behaves like iloc given integer
a   NaN
b   NaN
c   NaN
d   NaN
e   NaN
1   NaN

s2.ix[:6]는 에러를 내지 않고 iloc처럼 1-6번째 row를 반환한다. 또한 s2.ix[:'c']를 하면 loc처럼 1-3번째 row를 반환한다.

만일 label만 이용하던지, 아니면 integer position만 이용하던지 하나만 가지고 indexing하고자 한다면 iloc이나 loc중 하나를 사용하면 된다. 하지만 두 방법을 섞어서 쓰고 싶다면 반드시 ix를 사용해야한다. 예를 들면 다음과 같다.

>>> df = pd.DataFrame(np.arange(25).reshape(5,5), 
                      index=list('abcde'),
                      columns=['x','y','z', 8, 9])
>>> df
    x   y   z   8   9
a   0   1   2   3   4
b   5   6   7   8   9
c  10  11  12  13  14
d  15  16  17  18  19
e  20  21  22  23  24

mixed index를 사용하고 있는 DataFrame, df의 'c' 줄 x '8' 컬럼만 slicing하고자 한다면 ix를 통해서 다음과 같이 할 수 있다.

>>> df.ix[:'c', :4]
    x   y   z   8
a   0   1   2   3
b   5   6   7   8
c  10  11  12  13
