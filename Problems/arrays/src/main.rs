mod arrays;
use arrays::*;

fn main() {
    // Test your solutions
    let a = vec![1, 2, 2, 2, 2, 2, 2, 2, 2, 2];
    // let a = vec![1, 2, 3, 4, 5, 6];
    // let b = multiply_each_by_ten(&a);
    // println!("{:?}", b);

    search_for_an_element_first_occurance(&a, 2);

    // let avg = find_average(&a);
    // println!("{}", avg);
}
