import pytest
from StringUtils import StringUtils
@pytest.mark.parametrize ("wordm,wordz",[("skypro","Skypro"), ("Mamed","Mamed"),("MAMED","Mamed"),("MA MED","Ma med")])
def testzaglavnayapos (wordm,wordz):
    zaglavnaya= StringUtils()
    res=zaglavnaya.capitilize(wordm)
    assert res==wordz

@pytest.mark.parametrize ("wordm,wordz",[("123","123"), ("",""),(" "," ")])
def testzaglavnayaneg (wordm,wordz):
    zaglavnaya= StringUtils()
    res=zaglavnaya.capitilize(wordm)
    assert res==wordz

@pytest.mark.parametrize ("wordm,wordz",[("123","123"), ("",""),(" "," ")])
def testzaglavnayaneg (wordm,wordz):
    zaglavnaya= StringUtils()
    res=zaglavnaya.capitilize(wordm)
    assert res==wordz


@pytest.mark.parametrize ("wordm,wordz",[(" Mamed","Mamed"), (" mamed","mamed"),(" Mamed ","Mamed "),("  Mamed","Mamed"),(" Mamed Abdulaev","Mamed Abdulaev"),("                       M","M")])
def testtrimpoz (wordm,wordz):
    trim= StringUtils()
    res=trim.trim(wordm)
    assert res==wordz

@pytest.mark.parametrize ("wordm,wordz",[("  ",""), (" 123","123")])
def testtrimneg (wordm,wordz):
    trim= StringUtils()
    res=trim.trim(wordm)
    assert res==wordz

@pytest.mark.parametrize ("nespisok,delimeter,spisok",[("Каждый:охотник:желает",":",["Каждый","охотник","желает"]),("Понедельник,вторник,среда",",",["Понедельник","вторник","среда"]),("  ",",",[])])
def testtolist (nespisok,delimeter,spisok):
    to_list= StringUtils()
    res=to_list.to_list(nespisok,delimeter)
    assert res==spisok

@pytest.mark.parametrize ("word,liter",[("Mamed","m"),("123","2"),(" слово доброе","о")])
def testcontains (word,liter):
    contains= StringUtils()
    res=contains.contains(word,liter)
    assert res is True

@pytest.mark.parametrize ("list,joiner,string",[(["M","a","m","e","d"], ",", "M,a,m,e,d")])
def testliststring (list,joiner,string):
    liststr= StringUtils()
    res=liststr.list_to_string(list,joiner)
    assert res == string


    
