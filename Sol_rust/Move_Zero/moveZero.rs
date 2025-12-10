struct Solution;

impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {

        let mut revise_nums = Vec::new();

        if !nums.contains(&0) {
            println!("{:?}", nums);
            return;
        }

        for index in nums.iter() {
            if *index != 0 {
                revise_nums.push(index);
            }
        }
        for index_zero in nums.iter() {
            if *index_zero == 0 {
                revise_nums.push(index_zero);
            }
        }
        println!("{:?}", revise_nums);

        }
        
    }


fn main() {
    let mut nums = vec![0,0,0,5,7,3,12];
    Solution::move_zeroes(&mut nums);
}