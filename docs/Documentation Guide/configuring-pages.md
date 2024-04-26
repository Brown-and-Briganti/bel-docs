# Configuring Documentation Pages

## File name convention

Keeping a naming pattern within files helps:

* stay consistent across the docs
* easily identify which software or tool is being described

There is no specific file name convention. Our site organization keeps all related pages together in the same directory. Still, it should be relatively clear to other people what each file is or what topic it is associated with.

Using a commonly used shorthand (e.g., gmx for GROMACS) as a prefix followed by the name of the technique or tool is the simplest way to organize files independent of the directories. For example, for a page on calculating solvent accessible surface area (SASA) in GROMACS, you could name this file `gmx-sasa.md`.

## Updating the site navigation

New pages are not automatically added to the site navigation. To view your new page in the documentation, they must be manually added to the `mkdocs.yml` file in the (root) directory of the GitHub repository.

In `mkdocs.yml`, you will need to add the path to your page's MD file under the `nav` section. The `nav` section is a list, so make sure your new entry is spaced properly or the site will fail to compile. Paths used here are relative to the `docs/` directory.

The general format is:

```yaml
nav:
  - Home: index.md
  - Header 1:
    - Header 1/index.md
    - Section 1:
      - Section 1 page: path/to/page.md
      - Subsection 1:
        - path/to/page.md
    - Section 2:
      - ...
  - Header 2:
  - ...
```

![Navigation hierarchy depicting headers, sections, subsections, pages](../assets/user%20guide/docguide_01.png)

The above navigation has a hierarchy of headers, sections, subsections, then pages. Sections can be nested as much as you want, but try to maintain only three levels to avoid over-complicating the nav.

The highest level of the list will appear at the top of the site as a navigation tab. Clicking a navigation tab will bring you to the first file listed under that header.

---

Pages can be listed two ways: titled with a path, or as a path only.

```yaml
    - Subsection 1:
      - Page: path/to/page.md
      - path/to/page.md
```

Either format is acceptable. Titles not explicitly stated will be inferred from the first header of the page, which is helpful if you want to list the page differently than what is written in H1.


!!! note
    If a section has subsections, paths cannot be written on the same line as the section title. Subsequent pages must be added in the next line, otherwise the site will fail to compile.

## Additional Resources

* [MkDocs documentation on page configuration](https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation)