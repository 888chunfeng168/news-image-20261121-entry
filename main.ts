// news-image-20261121 entry (Node 22, standard library only).
//
// The entry image is entry.png, composed in this repository by
// compose.py from the freshly generated lead artwork (lead-art.png)
// plus crisp PIL-rendered lettering. This program only copies that
// finished image to the grader's output directory, so both runs
// write exactly the same bytes.
//
// Local check: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const source = new URL("./entry.png", import.meta.url);
if (!existsSync(source)) {
  throw new Error("entry.png is missing from the repository");
}
const target = join(outDir, "entry.png");
copyFileSync(source, target);
console.log(`wrote ${target}`);
