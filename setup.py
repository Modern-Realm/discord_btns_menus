import re
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("package/btns_menus/__init__.py") as f:
    search_v = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)

    if search_v is not None:
        version = search_v.group(1)
    else:
        raise RuntimeError("Error occurred while installing !\n"
                           "go to https://github.com/Modern-Realm/discord_btns_menus for more info ...")

setuptools.setup(
    name="discord-btns-menus",
    version=version,
    author="P. Sai Keerthan Reddy",
    author_email="saikeerthan.keerthan.9@gmail.com",
    description="A responsive package for Buttons, DropMenus, Combinations and Paginator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Modern-Realm/discord_btns_menus",
    project_urls={
        "Documentation": "https://modern-realm.github.io/discord_btns_menus/",
        "Bug Tracker": "https://github.com/Modern-Realm/discord_btns_menus/issues",
        "Examples": "https://github.com/Modern-Realm/discord_btns_menus/tree/main/Examples",
        "Source": "https://github.com/Modern-Realm/discord_btns_menus/tree/main/package/btns_menus",
        "Discord Server": "https://discord.gg/GVMWx5EaAN",
    },
    keywords=["py-cord", "pycord", "buttons", "dropmenus", "menus",
              "nextcord", "disnake", "discordpy"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    license="MIT",
    package_dir={"": "package"},
    packages=["btns_menus", "btns_menus.builds"],
    include_package_data=True,
    python_requires=">=3.8"
)
