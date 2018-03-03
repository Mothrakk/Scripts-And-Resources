namespace PySharp
{
    /// <summary>
    /// This class deals with communication between C# and Python
    /// </summary>
    public class PySharp
    {
        /// <summary>
        /// This method executes a Python script and returns the printed values, in case of failure, it writes errors to a file, refer to line 38
        /// </summary>
        /// <param name="python">Filepath to the Python interpreter, aka python.exe</param>
        /// <param name="args">Filepath to the script that you want to launch, including arguments (optional) to pass. Example: @"..\script.py 2 5", with 2 and 5 being the passed arguments.</param>
        /// <param name="CreateNoWindow">Set to false if you want the script's console to show up</param>
        /// <returns></returns>
        public static string ExecutePy(string python, string args, bool CreateNoWindow = true)
        {
            System.Diagnostics.ProcessStartInfo psi = new System.Diagnostics.ProcessStartInfo()
            {
                UseShellExecute = false,
                RedirectStandardOutput = true,
                RedirectStandardError = true,
                CreateNoWindow = CreateNoWindow,
                FileName = python,
                Arguments = args
            };
            System.Diagnostics.Process p = new System.Diagnostics.Process()
            {
                StartInfo = psi
            };

            p.Start();
            string contents = p.StandardOutput.ReadToEnd();
            string errors = p.StandardError.ReadToEnd();
            p.WaitForExit();
            p.Close();

            if(errors.Length > 0)
            {
                System.IO.File.WriteAllText(System.IO.Directory.GetCurrentDirectory() + @"\pysharp.log", errors);
                contents = "ERROR";
            }
            return (contents);
        }
    }
}