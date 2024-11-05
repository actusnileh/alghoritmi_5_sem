import { useState } from "react";
import { Container, Group, Burger, Title } from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import classes from "./HeaderMenu.module.css";

const links = [
    { link: "/", label: "🧮 №1" },
    { link: "/lab2", label: "➗ №2" },
    { link: "/lab3", label: "🎒 №3" },
    { link: "/lab4", label: "🔡 №4" },
    { link: "/lab5", label: "🌳 №5" },
    { link: "/lab6", label: "🌴 №6" },
];

export function HeaderMenu() {
    const [opened, { toggle }] = useDisclosure(false);
    const [active, setActive] = useState(window.location.pathname);

    const items = links.map((link) => (
        <a
            key={link.label}
            href={link.link}
            className={classes.link}
            data-active={active === link.link || undefined}
            onClick={(event) => {
                event.preventDefault();
                setActive(link.link);
                window.location.href = link.link;
            }}
        >
            {link.label}
        </a>
    ));

    return (
        <header className={classes.header}>
            <Container size="md" className={classes.inner}>
                <Title
                    style={{ cursor: "pointer" }}
                    order={3}
                    onClick={() => (window.location.href = "/")}
                >
                    Алгоритмы, построение и анализ
                </Title>
                <Group gap={5} visibleFrom="xs">
                    {items}
                </Group>

                <Burger
                    opened={opened}
                    onClick={toggle}
                    hiddenFrom="xs"
                    size="sm"
                />
            </Container>
        </header>
    );
}
