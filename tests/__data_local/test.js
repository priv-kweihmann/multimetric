import defaultExport from "module-name";
import * as name from "module-name";
import { export1 } from "module-name";
import { export1 as alias1 } from "module-name";
import { default as alias } from "module-name";
import { export1, export2 } from "module-name2";
import { export1, export2 as alias2 } from "module-name";
import { "string name" as alias } from "module-name3";
import defaultExport, { export1 } from "module-name";
import defaultExport, * as name from "module-name5";
import "module-name";

// Comment

function capitalize(stringToCapitalize) {
    return stringToCapitalize[0].toUpperCase() + stringToCapitalize.slice(1);
}

function main() {
    /* another comment */
    if (process.argv.length == 3 && process.argv[2].length > 0) {
        let input = process.argv[2];
        console.log(capitalize(input)); 
    } else {
        console.log("Usage: please provide a string");
    }
}

main();
