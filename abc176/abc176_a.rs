use ::proconio::input;
fn main() {
    input! {
        n : i128,
        x : i128,
        t : i128,
    }
    let ans: i128 = if n % x == 0 { n / x } else { n / x + 1 };
    println!("{}", ans * t);
}
