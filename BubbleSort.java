/**
 * 
 */
package com.interview.algorithms;

/**
 * @author Sarvani
 *
 */
public class BubbleSort {

	public static void main(String[] args) {
		int[] numbers = { -3, -5, 1, 7, 4, -2 };

		BubbleSort bs = new BubbleSort();
		int[] sortedNumbers = bs.bubbleSort(numbers);
		for (int i = 0; i < numbers.length; i++) {
			System.out.println(numbers[i]);
		}

	}

	public int[] bubbleSort(int[] numbers) {
		boolean numbersSwitched;
		do {
			numbersSwitched = false;
			for (int i = 0; i < numbers.length - 1; i++) {
				if (numbers[i + 1] > numbers[i]) {
					int tmp = numbers[i + 1];
					numbers[i + 1] = numbers[i];
					numbers[i] = tmp;
					numbersSwitched = true;
				}
			}
		} while (numbersSwitched);
		return numbers;
	}

}
