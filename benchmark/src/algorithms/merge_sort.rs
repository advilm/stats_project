// https://github.com/TheAlgorithms/Rust/blob/master/src/sorting/merge_sort.rs

// MIT License

// Copyright (c) 2019 The Algorithms

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

fn merge<T: Ord + Copy>(arr: &mut [T], mid: usize) {
    // Create temporary vectors to support the merge.
    let left_half = arr[..mid].to_vec();
    let right_half = arr[mid..].to_vec();

    // Indexes to track the positions while merging.
    let mut l = 0;
    let mut r = 0;

    for v in arr {
        // Choose either the smaller element, or from whichever vec is not exhausted.
        if r == right_half.len() || (l < left_half.len() && left_half[l] < right_half[r]) {
            *v = left_half[l];
            l += 1;
        } else {
            *v = right_half[r];
            r += 1;
        }
    }
}

pub fn merge_sort<T: Ord + Copy>(arr: &mut [T]) {
    if arr.len() > 1 {
        let mid = arr.len() / 2;
        // Sort the left half recursively.
        merge_sort(&mut arr[..mid]);
        // Sort the right half recursively.
        merge_sort(&mut arr[mid..]);
        // Combine the two halves.
        merge(arr, mid);
    }
}