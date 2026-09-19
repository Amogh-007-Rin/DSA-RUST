// Basic DSA Questions For Arrays 

// Question-1: Given an array, move all 0s to the end of it while maintaining the relative order of the non-zero elements

// Un-optimized solution with high space and time complexity
// Un-optimized solution has a space complexity of O(n)
pub fn _move_zeros_to_end_unoptimized(nums: &mut [i32])-> Vec<i32> {
    let mut zero_end_array: Vec<i32> = Vec::new();
    let mut zero_array: Vec<i32> = Vec::new();
    for (_index, num) in nums.iter().enumerate(){
        if !num.eq(&0){
            zero_end_array.push(*num);
        }
        else {
            zero_array.push(*num);
        }
    }
    for val in zero_array{
        zero_end_array.push(val);
    }

    return zero_end_array;
    
}

// Optimized Solution without copying or making new vectors
// Optimized Solution has the space complezity of O(1) -> constant 
pub fn _move_zeros_to_end_optimized(nums: &mut [i32]) -> &mut [i32]{

    let mut writer_index  = 0;

    // Step 1: Move all non-zero elements to the front
    for i in 0..nums.len(){
        if nums[i] != 0{
            nums[writer_index] = nums[i];
            writer_index+=1;
        }
    }

    // Step 2: Fill the remaining positions with zeros
    for i in writer_index..nums.len(){
        nums[i] = 0;
    }

    return nums;
}

// ------------------------------------------------------------------------------------//

// Question-2: 