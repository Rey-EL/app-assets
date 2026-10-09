# app-assets

I use this repo as a simple image host. It serves files through GitHub Pages so I can hotlink images in my other projects and READMEs.

## How it works

1. Drop image files into the `images/` folder.
2. Run `python deploy.py`.
3. The script commits, pushes, and prints a direct URL for every image:

```
https://Rey-EL.github.io/app-assets/images/your-image.png
```

Filenames with spaces or special characters get URL-encoded automatically.

Note: GitHub Pages needs to be enabled on this repo for the URLs to work.
