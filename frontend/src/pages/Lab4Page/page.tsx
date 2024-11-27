import { HeaderMenu, Lab4Window } from "../../components";
import { FC, useState } from "react";

export const Lab4Page: FC = () => {
    const [_, setValues] = useState<string>("");

    const handleValuesChange = (newValues: string) => {
        setValues(newValues);
    };

    return (
        <>
            <HeaderMenu />
            <Lab4Window onValuesChange={handleValuesChange} />
        </>
    );
};
