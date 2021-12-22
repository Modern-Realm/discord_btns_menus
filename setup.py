import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycord-btns-menus",
    version="0.1.7",
    author="P. Sai Keerthan Reddy",
    author_email="saikeerthan.keerthan.9@gmail.com",
    description="A responsive package for Buttons, DropMenus and Combinations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skrphenix/pycord_btns_menus",
    project_urls={
        "Documentation": "https://skrphenix.github.io/pycord_btns_menus/",
        "Bug Tracker": "https://github.com/skrphenix/pycord_btns_menus/issues",
        "Examples": "https://github.com/skrphenix/pycord_btns_menus/tree/main/Examples",
        "Source": "https://github.com/skrphenix/pycord_btns_menus/tree/main/package/btns_menus",
        "Support Server": "https://discord.gg/GVMWx5EaAN",
    },
    keywords=["pycord", "py-cord", "btns", "pycord buttons",
              "pycord btns", "pycord btns menus", "py-cord btns menus"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Buttons"
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    license="MIT",
    package_dir={"": "package"},
    packages=["btns_menus", "btns_menus.builds", "btns_menus.builds.base"],
    include_package_data=True,
    python_requires=">=3.6",
    dependency_links=[
        "https://github.com/Pycord-Development/pycord"
    ],
    install_requires=[
        "py-cord @ git+https://github.com/Pycord-Development/pycord@c8c2b1e23cb610b4c5f84c48fb23f279f2f0d53f"
    ]
)
