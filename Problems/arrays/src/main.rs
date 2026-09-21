mod arrays;
use arrays::*;

fn main() {
    // Test your solutions

    // let a = vec![1, 2, 3, 4, 5, -1, -2, -3, -4, -5];
    // let b = vec![1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0];
    // let ans = count_no_zeros_ones(a);
    // println!("{:?}", ans);
    // let un_sorted_arr = vec![1,2,3,4,5,11,12,13,17,16];
    // let ans = first_unsorted_element(un_sorted_arr);
    // println!("{:?}", ans);
    // println!("first unsorted element is: {} at index: {}", ans[0], ans[1]);
    // let arr = vec![0,1,2,2,4,5,6,7,10,27];
    // let max_value = get_minimum(arr);
    // println!("{}", max_value);

    let mut arr = vec![1,2,3,4];
    
    // swapped arr = [2,1,4,3]

    swap_alternate(&mut arr);
    print!("{:?}", arr);
    
    // let ans = sway_alternate(arr);
    // ans = [1,10,2,9,3,8,4,7,5,6]
    // print_alternate_extream_elements(arr);


}
