package com.sirxu

class myString(msg: String) {
    var raw:String = msg
    def len():Int = msg.length
    def unique():Boolean = {
        var checker:Int = 0
        raw.foreach(i => {
            var idx:Int = i-'a'
            if ((checker & (1<<idx))>0)
                return false
            checker |= (1<<idx)
        })
        return true
    }
    def isPermute(other:String):Boolean = {
        return raw.sorted == other.sorted
    }
    def isPermute2(other:String):Boolean = {
        var count = Array.fill[Int](256)(0)
        raw.foreach(i=> {
            count(i-'a') += 1
        })
        println(count)
        return true
    }
}
