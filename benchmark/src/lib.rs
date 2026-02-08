pub mod algorithms;

fn is_sorted<T: Ord>(arr: &[T]) -> bool
{
    arr.windows(2).all(|w| w[0] <= w[1])
}
