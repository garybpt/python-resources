# Connecting to your GitHub account on Visual Studio Code

To connect your GitHub account to Visual Studio Code (VS Code) on multiple computers, you need to follow these steps:

**Install VS Code:**

Ensure that you have Visual Studio Code installed on all the computers where you want to connect to your GitHub account. You can download and install VS Code from the official website: https://code.visualstudio.com/.

**Install the GitHub Extension for VS Code:**

You'll need the "GitHub Pull Requests and Issues" extension to easily integrate your GitHub account with VS Code. To install it, follow these steps:

- Open VS Code.
- Go to the Extensions view by clicking on the Extensions icon in the sidebar or by pressing Ctrl+Shift+X (Windows/Linux) or Cmd+Shift+X (macOS).
- Search for "GitHub" in the Extensions view search bar.
- Click the "Install" button next to the "GitHub" extension published by GitHub.

**Sign in to Your GitHub Account:**

Once the GitHub extension is installed, you can sign in to your GitHub account on each computer by following these steps:

- Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS) to open the command palette in VS Code.
- Type "GitHub: Sign In" and select it from the list of options.
- A web page will open, asking you to authorize VS Code's access to your GitHub account. Sign in with your GitHub credentials and authorize the access.

**Configure Remote Repositories:**

If you have repositories on GitHub that you want to access from VS Code on multiple computers, you can clone them using the "GitHub: Clone" command:

- Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS) to open the command palette.
- Type "GitHub: Clone" and select it.
- You'll be prompted to choose a repository from your GitHub account. Select the one you want to clone.
- Once you've cloned a repository on one computer, it will be available in VS Code on that computer. You can repeat the same process on other computers to clone the repository there as well.

**Syncing Changes:**

When you make changes to your code on one computer and push them to GitHub, those changes will be visible when you access the repository from any other computer where you've cloned it.

**Remember to Push and Pull:**

Ensure that you regularly push your changes to GitHub and pull changes from GitHub to keep your code in sync across multiple computers. You can do this using the Git integration within VS Code.

That's it! You should now be able to connect your GitHub account to VS Code on multiple computers and work on your repositories seamlessly.