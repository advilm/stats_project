use benchmark::algorithms::*;
use criterion::{black_box, criterion_group, criterion_main, Criterion};
use rand::{prelude::SliceRandom, thread_rng};

pub fn criterion_benchmark(c: &mut Criterion) {
    let mut rng = thread_rng();

    // c.bench_function("bogo_sort", |b| {
    //     b.iter(|| {
    //         let mut arr = (0..10).collect::<Vec<_>>();
    //         arr.shuffle(&mut rng);
    //         bogo_sort(black_box(&mut arr))
    //     })
    // });

    c.bench_function("bubble_sort", |b| {
        b.iter(|| {
            let mut arr = (0..1000).collect::<Vec<_>>();
            arr.shuffle(&mut rng);
            bubble_sort(black_box(&mut arr))
        })
    });

    c.bench_function("heap_sort", |b| {
        b.iter(|| {
            let mut arr = (0..1000).collect::<Vec<_>>();
            arr.shuffle(&mut rng);
            heap_sort(black_box(&mut arr))
        })
    });

    c.bench_function("insertion_sort", |b| {
        b.iter(|| {
            let mut arr = (0..1000).collect::<Vec<_>>();
            arr.shuffle(&mut rng);
            insertion_sort(black_box(&mut arr))
        })
    });

    c.bench_function("merge_sort", |b| {
        b.iter(|| {
            let mut arr = (0..1000).collect::<Vec<_>>();
            arr.shuffle(&mut rng);
            merge_sort(black_box(&mut arr))
        })
    });

    c.bench_function("quick_sort", |b| {
        b.iter(|| {
            let mut arr = (0..1000).collect::<Vec<_>>();
            arr.shuffle(&mut rng);
            quick_sort(black_box(&mut arr))
        })
    });

    c.bench_function("selection_sort", |b| {
        b.iter(|| {
            let mut arr = (0..1000).collect::<Vec<_>>();
            arr.shuffle(&mut rng);
            selection_sort(black_box(&mut arr))
        })
    });
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
