function Sidebar() {
  return (
    <aside className="w-64 bg-slate-800 border-r border-slate-700 p-6">
      <ul className="space-y-6 text-slate-300">

        <li className="hover:text-cyan-400 cursor-pointer">
          Dashboard
        </li>

        <li className="hover:text-cyan-400 cursor-pointer">
          Analytics
        </li>

        <li className="hover:text-cyan-400 cursor-pointer">
          About
        </li>

      </ul>
    </aside>
  );
}

export default Sidebar;