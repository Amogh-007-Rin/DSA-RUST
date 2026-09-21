// Basic DSA Questions For Arrays

// Question-1: Given an array, move all 0s to the end of it while maintaining the relative order of the non-zero elements

use std::{
    collections::{BTreeSet, HashSet},
    vec,
};

// Un-optimized solution with high space and time complexity
// Un-optimized solution has a space complexity of O(n)
pub fn move_zeros_to_end_unoptimized(nums: &mut [i32]) -> Vec<i32> {
    let mut zero_end_array: Vec<i32> = Vec::new();
    let mut zero_array: Vec<i32> = Vec::new();
    for (_index, num) in nums.iter().enumerate() {
        if !num.eq(&0) {
            zero_end_array.push(*num);
        } else {
            zero_array.push(*num);
        }
    }
    for val in zero_array {
        zero_end_array.push(val);
    }

    return zero_end_array;
}

// Optimized Solution without copying or making new vectors
// Optimized Solution has the space complezity of O(1) -> constant
pub fn _move_zeros_to_end_optimized(nums: &mut [i32]) -> &mut [i32] {
    let mut writer_index = 0;

    // Step 1: Move all non-zero elements to the front
    for i in 0..nums.len() {
        if nums[i] != 0 {
            nums[writer_index] = nums[i];
            writer_index += 1;
        }
    }

    // Step 2: Fill the remaining positions with zeros
    for i in writer_index..nums.len() {
        nums[i] = 0;
    }

    return nums;
}

// ------------------------------------------------------------------------------------//

// Question-2: Find the average of array elements
pub fn find_average(arr: &[u32]) -> f32 {
    if arr.is_empty() {
        return 0.0;
    }

    let mut sum: u32 = 0;
    let n = arr.len();

    for num in arr {
        sum = sum + *num;
    }

    let avg = (sum as f32) / (n as f32);

    println!("sum is: {}, n is : {}, avg is :{}", sum, n, avg);
    return avg;
}

// ------------------------------------------------------------------------------------//

// Question-3: Multiply each element of array by 10
pub fn multiply_each_by_ten(arr: &[u32]) -> Vec<u32> {
    let mut new_arr: Vec<u32> = Vec::new();

    for value in arr {
        new_arr.push(value * 10);
    }

    return new_arr;
}
// ------------------------------------------------------------------------------------//

// Question-4.a: Search for an element in an Array for all the index {Linear Search}
pub fn search_for_an_element(arr: &[u32], element: u32) {
    if arr.is_empty() {
        println!("The array is empty");
    }

    for (index, value) in arr.iter().enumerate() {
        if value.eq(&element) {
            println!("value: {}, found at index: {}", value, index);
        }
    }
}

// Question-4.b: Search for an element in an Array for its first presence with the index {Linear Search}
pub fn search_for_an_element_first_occurance(arr: &[u32], element: u32) {
    if arr.is_empty() {
        println!("The array is empty");
    }

    for (index, value) in arr.iter().enumerate() {
        if value.eq(&element) {
            println!("value: {}, found at index: {}", value, index);
            break;
        }
    }
}
// ------------------------------------------------------------------------------------//

// Question-5: Return the sum of positive and negative numbers

pub fn positive_negative_sum(arr: Vec<i32>) -> Vec<i32> {
    let mut positive_sum = 0;
    let mut negative_sum = 0;

    for value in arr {
        if value >= 0 {
            positive_sum = positive_sum + value;
        } else {
            negative_sum = negative_sum + value;
        }
    }

    let ans = vec![positive_sum, negative_sum];
    return ans;
}

// ------------------------------------------------------------------------------------//
// Question-6: count the number of zeros and ones present in an array
pub fn count_no_zeros_ones(arr: Vec<i32>) -> Vec<i32> {
    let mut ones = 0;
    let mut zeros = 0;

    for value in arr {
        if value.eq(&1) {
            ones += 1;
        } else if value.eq(&0) {
            zeros += 1;
        }
    }

    let ans = vec![ones, zeros];
    return ans;
}

pub fn first_unsorted_element(arr: Vec<i32>) -> Vec<i32> {
    for (i, v) in arr.iter().enumerate() {
        if arr[i] > arr[i + 1] {
            let ans = vec![*v as i32, i as i32];
            return ans;
        }
    }
    return vec![];
}

// ------------------------------------------------------------------------------------//

// Question-7: Find maximum value element in an array

pub fn get_maximum(arr: Vec<i32>) -> i32 {
    let mut max_value = arr[0];

    for value in arr {
        if value >= max_value {
            max_value = value;
        }
    }

    return max_value;
}

/*

    Test case:
    let arr = vec![1,2,2,4,5,6,7,10,27];
    let max_value = get_maximum(arr);
    println!("{}", max_value);

*/

// ------------------------------------------------------------------------------------//

// Question-8: Find minimum value element in an array
pub fn get_minimum(arr: Vec<i32>) -> i32 {
    let mut min_value = arr[0];
    for value in arr {
        if value <= min_value {
            min_value = value;
        }
    }

    return min_value;
}

// ------------------------------------------------------------------------------------//

/*

    Test case:
    let arr = vec![1,2,2,4,5,6,7,10,27];
    let min_value = get_maximum(arr);
    println!("{}", min_value);

*/

// Question-9: Swap Alternate Elements in an Array

// let arr = vec![1,2,3,4];

// swapped arr = [2,1,4,3]

pub fn swap_alternate(arr: &mut [i32]) {
    let mut i = 0;
    let length = arr.len();

    // i + 1 here is to ensure we have a valid pair to swap (stop before the last element if length is oddi)
    while i + 1 < length {
        // Step-1: copy the first element into a temporary location

        let temp = arr[i];

        // Step-2: Overwrite the first element out into a temproary location

        arr[i] = arr[i + 1];

        // Step-3: Overwrite the second element with the saved temproary value

        arr[i + 1] = temp;

        // Step-4: Move forward by 2 to jump to the next pair
        i += 2;
    }
}

// Question-10: Print Array union element

pub fn print_array_union(arr: Vec<i32>, brr: Vec<i32>) -> Vec<i32> {
    let mut union: HashSet<i32> = HashSet::new();

    for a in arr {
        union.insert(a);
    }

    for b in brr {
        union.insert(b);
    }

    let ans: Vec<i32> = union.into_iter().collect();
    return ans;
}

// Question-11: Print Array intersection element

pub fn print_array_intersection(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
    let mut intersection: BTreeSet<i32> = BTreeSet::new();

    if a.is_empty() && b.is_empty() {
        return vec![];
    }

    for i in a {
        for j in b.clone() {
            if i == j {
                intersection.insert(i);
            }
        }
    }
    let ans: Vec<i32> = intersection.into_iter().collect();
    return ans;
}

/*
    let a = vec![1,2,3,4,5,22,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,3,1,1,11,12,14];
    let b = vec![1,2,3,4,5];
    let ans = print_array_intersection(a, b);
    println!("{:?}", ans);
*/

pub fn print_alternate_extream_elements(arr: Vec<i32>) {
    let l = arr.len();
    let mut counter = 0;

    for (i, v) in arr.iter().enumerate() {
        if counter < l / 2 {
            print!("{} ", arr[i]);
            print!("{} ", arr[l - i - 1]);
        }
        counter += 1;
    }
}
