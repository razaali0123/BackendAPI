const App = () => {
  return (
    <div className="container grid h-screen place-items-center bg-gradient-to-tr from-slate-600 via-slate-400 to-slate-600">
      <div className="flex h-auto min-w-fit flex-col items-center justify-center rounded-xl bg-white p-11 shadow-md shadow-slate-800">
        <h1 className="mb-4 text-2xl font-semibold text-slate-800 ">Login</h1>
        <input
          className="mx-4 mb-2 rounded bg-slate-200 p-1"
          type="text"
          placeholder="Username"
        />
        <input
          className="mx-4 rounded bg-slate-200 p-1"
          type="password"
          name="password"
          id="password"
          placeholder="Password"
        />
        <button
          className="m-2 w-10/12 rounded-lg bg-slate-400 p-1"
          type="submit"
        >
          Submit
        </button>
      </div>
    </div>
  );
};

export default App;
