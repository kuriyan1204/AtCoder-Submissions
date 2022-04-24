use ::proconio::input;
use std::f64::consts::PI;
fn main() {
    input! {
        R : f64,
    }
    let ans: f64 = 2.0 * PI * R;
    println!("{}", ans);
}
