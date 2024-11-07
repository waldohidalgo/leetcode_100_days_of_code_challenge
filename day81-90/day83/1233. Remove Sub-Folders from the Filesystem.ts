function removeSubfolders(folder: string[]): string[] {
  folder.sort();
  let res: string[] = [folder[0]];
  for (let i = 1; i < folder.length; i++) {
    if (folder[i].startsWith(res[res.length - 1] + "/")) {
      continue;
    }
    res.push(folder[i]);
  }
  return res;
}
