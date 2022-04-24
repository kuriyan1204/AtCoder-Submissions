use ::proconio::input;
fn main() {
    input! {
        a : i128,
    }
    let ans: i128 = a + a * a + a * a * a;
    println!("{}", ans);
}
