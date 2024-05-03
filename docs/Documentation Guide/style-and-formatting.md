# Style and Formatting

## Introduction

This documentation serves to host various guides on techniques and tools used in the lab, but is not in itself an academic article. As such, these pages do not necessarily follow a strict style. However, there are still some general guidelines contributors should follow in order to keep pages clear and consistent across writers.

## Voice and tone

The voice and tone of these pages should be overall instructional but not clinical. Imagine you are working with and guiding someone through a process, or that you are giving a presentation to a class.

**Generally:**

* make sure it's clear what you are referring to when using ambiguous terms like "this", "it", "these" - especially in articles about complex topics
* aim for a conversational tone, but avoid overly casual
* avoid language that assumes skill or knowledge (e.g., simply, naturally, clearly)
* avoid starting sentences the same way ("to do X...") or repetitive sentence structure

Overall, prioritize readability and clarity. Section content does not need to be overly prosy, but also try to avoid sounding like you've written a recipe. Very long articles or user guides (like this page) may naturally end up prose-like, but you can be as concise as needed.

---

The following resources have helpful guiding points if you need extra direction:

* The *Voice and tone* section of the [GNOME developer documentation](https://developer.gnome.org/documentation/guidelines/devel-docs.html#voice-and-tone)
* [The Mozilla MDN documentation](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide)
* [Creating effective technical documentation (Mozilla)](https://developer.mozilla.org/en-US/blog/technical-writing/)
  
Although we are not necessarily writing developer documentation, the advice in these guides are still generally applicable.

## General formatting guidelines

### Article sections and organization

Articles should begin with a brief introduction that summarizes the content. This does not need to be more than a few sentences. The introduction should include information important for understanding the technique or tool, at least on a practical level. It should also list any additional files or software needed to follow the guide.

**Some questions to help you get started:**

* What are the key points of this guide?
* What does this tell us? Why do we care?
* If you were to write an FAQ on the topic, what would students ask you? Of these, what would the be *most critical* to know?

The rest of the article should be split into logical sections, whether sequential or otherwise grouped. This will typically be a step-by-step format.

While not required, it is helpful to add an "Additional Resources" section at the end of pages to include any external resources you think might be useful for understanding.

### Section and subsection titles

Titles displayed in the navigation should be in title case. Section and subsection titles within an article should be in sentence case.

The point of each section should be obvious from the title so readers can jump around if they need to. Whenever possible, sections that are describing a process should be titled as an action ("Updating the navigation").

#### Formatting the table of contents

The table of contents will update automatically if the appropriate Markdown heading formatting is used. The top level heading (`H1`) will be used as the page's title in the navigation unless otherwise noted in the [`mkdocs.yml` file](configuring-pages.md/#updating-the-site-navigation). Sections should use level 2 (`H2`) headings and higher.

```md
# H1 - Page title
## H2 - Section
### H3 - Subsection
#### H4 - Sub-subsection
...
```

### Section content

These guides will usually try to teach readers how to do something. Consider the following questions:

* Are there any tricky aspects of the technique or tool?
* What are some common issues, and how can they be avoided?

A lot of confusion stems from readers not understanding what is functionally happening when they use a script or enter a command. Include examples [(images, scenarios, etc.)](#text-styling-and-assets) if it would help with understanding. Split paragraphs into smaller sections to make them easier to digest, if needed. Remember, you don't need to explain every detail of a process, but it can be helpful to elaborate if readers are likely to hit roadblocks.

### Text styling and assets

Text styling includes hyperlinking, code blocks, and other visual effects outside of the typical bold, italic, and underline. MkDocs has some quirks with special styles—the most common of which are described below, along with general style recommendations. As always, visit the [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/reference/) for more information.

All assets (images, scripts, etc.) should be saved into the appropriately named directory under `docs/assets/`. In most cases, the relevant directory will already exist. If it does not exist, be sure to make one.

#### Splitting sections with horizontal breaks

Sometimes sections contain a lot of information that cannot easily be split into subsections, causing confusing visual clutter. You can use horizontal breaks (---) to visually isolate content:

```md
Words words words

---

Words words words
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Words words words

---

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Words words words

There must be an empty line before and after the dashes to render a horizontal break, otherwise Markdown will treat the preceding text like a `H2` heading.

#### Styling code blocks and in-line code

You can create a code block by wrapping text with two lines of three backticks (\`\`\`). Metadata such as line numbers, [syntax highlighting](https://pygments.org/docs/lexers/), and titles are included immediately after the first set of backticks. Some common language codes for syntax highlighting are `python/py`, `bash/sh`, `r`, and `markdown/md`.

````
```python title="Titled code block" linenums="1 (or other line # to start)"
import matplotlib.pyplot as plt
import pandas as pd
```
````

```python title="Titled codeblock" linenums="1"
import matplotlib.pyplot as plt
import pandas as pd
```

Line numbers, syntax highlighting, and titles are optional and can be omitted. 

!!! note
    Unfortunately, any single line of code that is too long will require scrolling to view the entire code block. This is a limitation of Markdown. Keep this in mind for especially long commands requiring multiple inputs or outputs!

Long or whole scripts are [handled differently](#adding-code-and-scripts) and should **not** be in a code block.

---

In-line snippets of code can be styled by surrounding the text with a single backtick (`). These are useful when talking about command or menu options.

```
This is `code`.
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is `code`.

##### Software-specific or command line code

When writing commands that involve inputs or outputs that will differ between projects, try to use a standard name or suggest a naming convention for clarity.

| Instead of:                             | Try:                         |
| --------------------------------------- | ---------------------------- |
| `gmx rmsf -f AbCeeD_replicate3_mol.xtc` | `gmx rmsf -f trajectory.xtc` |

---

Some software, such as GROMACS, and command lines use code that have additional options (e.g., `-help`). These are typically not required but may sometimes be useful.

You can include these options below the code block using [MkDocs admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/):

```md
???+ tip "Title of the admonition"

    * `First option`: description of option
    * ...
```

???+ tip "Title of the admonition"

    * `First option`: short description of option
    * ...

This specific admonition type is expandable and automatically opened on page load-in, giving readers the option to close and ignore them if needed.

If options need to be explained, include a short blurb below the code block or admonition. One example of this can be seen in the [GROMACS RMS guide](../Molecular%20Dynamics/GROMACS/gmx-rms.md/#using-gmx-rmsf).

##### Commands that produce outputs

Similar to above, if a command produces file outputs, try to directly list and describe each if more than one is expected:

!!! quote ""
    This produces the following outputs:

    * `-option`: short description of output

The short description can be pulled directly from the relevant documentation pages. This is especially helpful for commands with ambiguously named output options, and isn't necessary for commands with one output.

#### Linking to pages

Links use basic Markdown formatting and can be used in most special MkDocs formatting, including admonitions and [annotations](https://squidfunk.github.io/mkdocs-material/reference/annotations/). Links should be integrated into the text as much as possible.

The general format for a link is:

```md
[Text to be hyperlinked](link)
```

---

Try to avoid standalone or "link" links:

```md
https://veryreallink.towebpage.com/

You can find the script here: [link](link to script)
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;https://veryreallink.towebpage.com/

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can find the script here: [link](link to script)

---

When in doubt, or in the absence of appropriate text, format links like:

```md
You can find the script [here](link to script).
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;You can find the script [here](link to script).

#### Adding images and videos

While image embedding is natively supported, video embeds are not. If you want to include a video, you may need to link the file directly using link formatting, or save the video to our repository and redirect to the relevant directory.

---

Images can be embedded in two ways, depending on whether you want to include a caption, set its page alignment, or adjust its size.

The first way only uses Markdown:

```md
![Image title](path or link to image){ align=left/right }
```

The image title functions as alt text and is only displayed if the image cannot be loaded. Image titles should be descriptive but brief, especially if no caption is added.

The alignment attribute is optional and can be omitted. Images are left-aligned by default. Note that Markdown's `align` attribute does not support center alignment.

---

The second way can be used to *center align* or *add a caption*. This method wraps additional HTML tags around the Markdown:

```html
<figure markdown="span">
  ![Image title](path or link to image){ width="integer or percentage" }
  <figcaption>Image caption.</figcaption>
</figure>
```

This allows us to add image captions and dictate image size. By default, images embedded this way are center aligned. Both resizing and adding captions are optional and can be omitted. Since image captions are optional, we can also use this method to bypass the `align` limitations.

#### Adding code and scripts

For now, scripts and interactive Jupyter Notebooks are kept in the appropriate `assets/` folder. These can be linked to directly using basic link formatting, or redirect readers to the relevant directory in the GitHub repository. Direct links to scripts will bring up a save prompt when clicked.

Note that these are not the same as [code blocks](#styling-code-blocks-and-in-line-code).

## Additional Resources

* [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/reference/)
* [Creating effective technical documentation (Mozilla)](https://developer.mozilla.org/en-US/blog/technical-writing/)