use ::proconio::input;
fn main() {
    input! {
        a : i128,
        b : i128,
    }
    let max = 2 * a + 100;
    println!("{}", max - b);
}
