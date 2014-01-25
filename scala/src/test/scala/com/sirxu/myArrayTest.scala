package com.sirxu

import org.specs._

object myArrayTest extends Specification {
    val my = new myString("abcdefg")
    "myString" should {
        "dummy" in { 1+1 mustEqual 2}
        "length" in {
            my.len() mustEqual 7
        }
        "array" in {
            my.raw(0) mustEqual 'a'
        }
        "unique" in {
            var test1 = new myString("abcdef")
            test1.unique() mustEqual true
            var test2 = new myString("aecdef")
            test2.unique() mustEqual false
        }
        "isPermute" in {
            var test1 = new myString("dog")
            test1.isPermute("god") mustEqual true
            test1.isPermute("dod") mustEqual false
        }

    }
}
