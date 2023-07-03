const std = @import("std");
const print = @import("std").debug.print;

pub fn main() !void {
    /// doc comment
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello, {}!\n", .{"world"});
}

// comment