struct Solution;

impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut left = 0;
        let mut right = s.len() -1;

        while left < right {
            println!("reverse S = {}", s[right]);
            right -= 1;
        }
    }
}

fn main() {
    let mut s = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g'];
    Solution::reverse_string(&mut s);
}