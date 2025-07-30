import React from 'react';

type Props = {
  displayName: string;
};

const Greeting: React.FC<Props> = ({ displayName }) => (
  <h1>Hello, {displayName}!</h1>
);

export default Greeting;
