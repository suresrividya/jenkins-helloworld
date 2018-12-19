/**
 * 
 */
package com.interview.algorithms.test;

/**
 * @author Sarvani
 *
 */
public class EqualsTest {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str1 = new String("ABCD");
		String str2 = new String("ABCD");

		if (str1 == str2) {
			System.out.println("Str1 == Str2 is true");
		}

		else {
			System.out.println("Str1 == Str2 is false");
		}
		String str3 = str2;
		if (str3 == str2) {
			System.out.println("str3 == str2 is true");
		}

		else {
			System.out.println("str3==str2 is false");
		}
		if (str1.equals(str2)) {
			System.out.println("str1 is equal to str2");
		} else {
			System.out.println("str1 is not equal to str2");
		}
	}

}
