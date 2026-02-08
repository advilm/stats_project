use benchmark::algorithms::*;
use criterion::{black_box, criterion_group, criterion_main, Criterion};

pub fn criterion_benchmark(c: &mut Criterion) {
    // c.bench_function("sorted_bogo_sort", |b| {
    //     b.iter(|| bogo_sort(black_box(&mut (0..1000).collect::<Vec<_>>())))
    // });

    c.bench_function("sorted_bubble_sort", |b| {
        b.iter(|| bubble_sort(black_box(&mut (0..1000).collect::<Vec<_>>())))
    });

    c.bench_function("sorted_heap_sort", |b| {
        b.iter(|| heap_sort(black_box(&mut (0..1000).collect::<Vec<_>>())))
    });

    c.bench_function("sorted_insertion_sort", |b| {
        b.iter(|| insertion_sort(black_box(&mut (0..1000).collect::<Vec<_>>())))
    });

    c.bench_function("sorted_merge_sort", |b| {
        b.iter(|| merge_sort(black_box(&mut (0..1000).collect::<Vec<_>>())))
    });

    c.bench_function("sorted_quick_sort", |b| {
        b.iter(|| quick_sort(black_box(&mut (0..1000).collect::<Vec<_>>())))
    });

    c.bench_function("sorted_selection_sort", |b| {
        b.iter(|| selection_sort(black_box(&mut (0..1000).collect::<Vec<_>>())))
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
