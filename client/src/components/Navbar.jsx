import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="bg-gray-800 text-white p-4">
      <ul className="flex gap-4">
        <li><Link to="/" className="hover:underline">Home</Link></li>
        <li><Link to="/products" className="hover:underline">Products</Link></li>
        <li><Link to="/login" className="hover:underline">Login</Link></li>
        <li><Link to="/register" className="hover:underline">Register</Link></li>
      </ul>
    </nav>
  );
}
