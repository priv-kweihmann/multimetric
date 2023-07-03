<?php

include 'filename';
include_once 'other_file';
require '3rd';
require_once 'filename';

if ($argc < 2 || !is_numeric($argv[1])) {
    die("Usage: please input a number\n");
}

// This is a comment

$input = abs($argv[1]);

if ($input % 2 == 0) {
    echo "Even\n";
} elseif ($input % 2 == 1) {
    echo "Odd\n";
}
